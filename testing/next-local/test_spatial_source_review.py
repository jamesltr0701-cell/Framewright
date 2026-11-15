"""Check spatial source evidence through the existing shot-local validator."""

import unittest

from test_source_review import VALIDATOR, trace


def spatial_trace():
    result = trace()
    blocks = {
        'rear': '椅背后朝屏拍，甲画左靠内墙，乙画右靠窗。椅子正对前方大屏。',
        'front': '切到大屏方向朝人物拍，乙画左靠窗，甲画右靠内墙。',
        'wide': '同侧放宽，乙仍靠窗，甲仍靠内墙。大屏在两把椅子的前方、机位后方。',
    }
    result['prompt_shots'] = blocks
    result['prompt'] = '\n'.join(blocks.values())
    result['semantic_trace'] = [{
        'intent_id': 'fixed_seats_and_screen',
        'source_locator': 'review fixture / approved room and camera views',
        'source_excerpt': '甲靠内墙，乙靠窗，两椅朝屏。背拍甲左乙右，从屏侧拍脸乙左甲右。',
        'source_scope': list(blocks),
        'affected_shots_or_phases': list(blocks),
        'requirement_type': 'reference_state',
        'treatment': 'preserve',
        'rationale': 'Keep the approved room arrangement through each resolved camera view.',
        'preservation_status': 'preserved',
        'model_facing_carrier': [
            {'shot_id': shot, 'role': 'constraint', 'span': block}
            for shot, block in blocks.items()
        ],
    }]
    return result


class SpatialSourceReviewTests(unittest.TestCase):
    def test_opposite_views_preserve_fixed_seats(self):
        self.assertEqual(VALIDATOR.validate_source_review(spatial_trace()), [])

    def test_spatial_clauses_cannot_drift_after_review(self):
        cases = [
            ('rear', '甲画左靠内墙，乙画右靠窗', '乙画左靠内墙，甲画右靠窗'),
            ('front', '乙画左靠窗，甲画右靠内墙', '甲画左靠窗，乙画右靠内墙'),
            ('wide', '大屏在两把椅子的前方、机位后方', '大屏在两把椅子的背后'),
        ]
        for shot, old, new in cases:
            with self.subTest(shot=shot):
                data = spatial_trace()
                data['prompt_shots'][shot] = data['prompt_shots'][shot].replace(old, new)
                data['prompt'] = '\n'.join(data['prompt_shots'].values())
                codes = {issue['code'] for issue in VALIDATOR.validate_source_review(data)}
                self.assertIn('source_review_span_missing', codes)

    def test_every_affected_view_needs_local_evidence(self):
        data = spatial_trace()
        data['semantic_trace'][0]['model_facing_carrier'].pop()
        codes = {issue['code'] for issue in VALIDATOR.validate_source_review(data)}
        self.assertIn('source_review_affected_uncovered', codes)

    def test_span_validation_requires_prior_semantic_review(self):
        data = spatial_trace()
        wrong = '椅背后朝屏拍，乙画左靠内墙，甲画右靠窗。'
        data['prompt_shots']['rear'] = wrong
        data['prompt'] = '\n'.join(data['prompt_shots'].values())
        data['semantic_trace'][0]['model_facing_carrier'][0]['span'] = wrong
        # Matching a false claim to its own text cannot establish correct geometry.
        self.assertEqual(VALIDATOR.validate_source_review(data), [])


if __name__ == '__main__':
    unittest.main()
