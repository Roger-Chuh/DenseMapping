"""
Extract superpixels
"""

from superpixel_seed import SuperpixelSeed

def extract_superpixels(image, depth):
    """Extracts superpixels from an RGB image and depth image
    Arguments:
        image:  input image (nxmx3)
        depth:  depth image (nxm)
    Returns:
        supepixels: list of SuperpixelSeed
    """
    return None

def init_seeds(dims, sp_size=8):
    """Initializes the centers for the superpixels
    Arguments:
        dims:   dimensions of image, in tuple form heightxwidth, i.e. (480, 640)
    Returns:
        superpixels:    list of SuperpixelSeed, has correct x, y (others init to
            0)
    """
    return None

def assign_pixels(image, depth, superpixels):
    """Assigns each pixel in an image to a superpixel seed
    Arguments:
        image:  input image (nxmx3)
        depth:  depth image (nxm)
        superpixels:    list of SuperpixelSeed
    Returns:
        pixels:    nxm array of indices, where nxm is the size of the image and
            each element in the array represents the index of the superpixel
            which that pixel in the image is assigned to
    """
    return None

def update_seeds(image, depth, pixels, superpixels):
    """Updates the locations of the superpixel seeds
    Arguments:
        image:  input image (nxmx3)
        depth:  depth image (nxm)
        pixels: array of indices (nxm) which assigns each pixel to the index in 
            `superpixels` of the superpixel under which this pixel falls
        superpixels:    list of SuperpixelSeed
    Returns:
        superpixels:    list of SuperpixelSeed with updated positions
    """
    return None

def calc_norms(image, depth, pixels, superpixels):
    """Calculates the norms
    Arguments:
        image:  input image (nxmx3)
        depth:  depth image (nxm)
        pixels: array of indices (nxm) which assigns each pixel to the index in 
            `superpixels` of the superpixel under which this pixel falls
        superpixels:    list of SuperpixelSeed
    Returns:
        superpixels:    list of SuperpixelSeed with updated norms
    """
    return None

if __name__ == "__main__":
    pass