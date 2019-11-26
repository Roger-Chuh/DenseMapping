"""Test Surfel Generation."""
import unittest

from surfel_generation import SurfelGeneration
from superpixel_seed import SuperpixelSeed
import numpy as np
from mock import patch

with patch.object(SurfelGeneration, "__init__", lambda x1, x2, x3, x4: None):
    surfel_generation_instance = SurfelGeneration(None, None, None)


class TestSurfelGeneration(unittest.TestCase):
    # @unittest.skip("skip test_create_surfels")
    def test_create_surfels(self):
        """Test initialize Surfels from superpixels."""
        # initialize_surfels
        x, y = 1, 1
        size = 2
        norm_x, norm_y, norm_z = [1,1,1]
        position_x, position_y, position_z = [1,1,1]
        view_cos = 0.1
        mean_depth = 5
        mean_intensity = 100
        fused = False
        stable = True
        min_eigen_value = 10
        max_eigen_value = 10
        superpixel_1 = SuperpixelSeed(x, y, size, norm_x, norm_y, norm_z, position_x, position_y, position_z,
                                      view_cos, mean_depth, mean_intensity, fused, stable, min_eigen_value, max_eigen_value)
        superpixel_2 = SuperpixelSeed(x, y, size, norm_x, norm_y, norm_z, position_x, position_y, position_z,
                                      view_cos, mean_depth, mean_intensity, fused, stable, min_eigen_value, max_eigen_value)
        superpixels = [superpixel_1, superpixel_2]

        surfel_generation_instance.MAX_ANGLE_COS = 0.1
        surfel_generation_instance.all_surfels = []
        surfel_generation_instance.fx = 1
        surfel_generation_instance.fy = 1
        surfel_generation_instance.VERBOSE = False

        surfel_generation_instance.create_surfels(1, superpixels)
        pass

    # @unittest.skip("skip test_update_surfels")
    def test_update_surfels(self):
        "Test update surfels"
        sg = surfel_generation_instance
        sp = SuperpixelSeed(0, 0, 1,
                            0, 0, 1,
                            0, 0, 1, 0, 0, 0, 0, 0, 0, 0)
        pose0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                          [0, 0, 1, 0], [0, 0, 0, 1]])
        sg.update_surfels([sp], pose0)
        # identical surfel should be fused
        self.assertEqual(len(sg.all_surfels), 1)
        sg.update_surfels([sp], pose0)
        # surfel in same location and norm should be fused
        self.assertEqual(len(sg.all_surfels), 1)
        sp.posi_x = 1
        sp.posi_z = 0
        sp.norm_x = 1
        sp.norm_z = 0
        pose1 = np.array([[0, 0, -1, 0], [0, 1, 0, 0],
                          [1, 0, 0, 0], [0, 0, 0, 1]])
        sg.update_surfels([sp], pose1)
        self.assertEqual(len(sg.all_surfels), 1)
        # surfel in same location but different norm should NOT be fused
        sp.norm_x = 0
        sp.norm_z = 1
        sg.update_surfels([sp], pose1)
        self.assertEqual(len(sg.all_surfels), 2)
        # surfel in different location and different norm should NOT be fused
        sg.update_surfels([sp], pose0)
        self.assertEqual(len(sg.all_surfels), 3)


if __name__ == '__main__':
    unittest.main()
