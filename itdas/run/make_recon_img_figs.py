"""
Tyson Reimer
University of Manitoba
January 31st, 2020
"""

import os

from umbms import get_proj_path, verify_path, get_script_logger, null_logger
from umbms.loadsave import load_pickle

from imgplots import plot_img
from extras import apply_ant_t_delay

###############################################################################

# Directory where the geometry parameters are stored
__GEOM_PARAM_DIR = os.path.join(get_proj_path(), 'data/')

# Directory where the reconstructed images are
__DATA_DIR = os.path.join(get_proj_path(), 'output/recon-imgs/')

# Directory where the figures will be stored as .png files
__OUT_DIR = os.path.join(get_proj_path(), 'output/recon-img-figs/')
verify_path(__OUT_DIR)

###############################################################################


def make_recon_figs(logger=null_logger):
    """Plots all reconstructed images, saves each as a .png file

    Parameters
    ----------
    logger : logging object
        Logging object for logging the progress
    """

    # Load the geometry parameters of each scan in the dataset
    geom_params = load_pickle(os.path.join(__GEOM_PARAM_DIR,
                                           'geom_params.pickle'))

    # Load the reconstructed images
    das_imgs = load_pickle(os.path.join(__DATA_DIR, 'das_imgs.pickle'))
    dmas_imgs = load_pickle(os.path.join(__DATA_DIR, 'dmas_imgs.pickle'))
    itdas_imgs = load_pickle(os.path.join(__DATA_DIR, 'itdas_imgs.pickle'))
    itdmas_imgs = load_pickle(os.path.join(__DATA_DIR, 'itdmas_imgs.pickle'))


    expt_id = 'c2sf3cm'

    logger.info('\tMaking figs for expt id:\t%s' % expt_id)

    # Get the geometry parameters from the scan
    # tum_x, tum_y, tum_rad, adi_rad, ant_rad = geom_params[expt_id]
    # print(geom_params[expt_id])

    # scan 112
    tum_x = -0.0225
    tum_y = -0.03
    tum_rad = 0.01
    adi_rad = 0.06 #radius A1
    ant_rad = 0.21
    ant_rad = apply_ant_t_delay(ant_rad)  # Correct for time delay

    # Plot DAS image
    plot_img(das_imgs[expt_id], tum_x=tum_x, tum_y=tum_y, tum_rad=tum_rad,
                adi_rad=adi_rad, ant_rad=ant_rad,
                save_fig=True,
                save_str=os.path.join(__OUT_DIR, 'das_%s.png' % expt_id),
                title='DAS Reconstruction')


###############################################################################


if __name__ == "__main__":

    logger = get_script_logger(__file__)

    logger.info("Beginning...Plotting of All Reconstruted Images...")

    make_recon_figs(logger=logger)
