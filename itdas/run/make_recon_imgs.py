"""
Tyson Reimer
University of Manitoba
January 14th, 2020
"""

import os
import pandas as pd
import csv

from umbms import get_proj_path, verify_path, get_script_logger, null_logger
from umbms.loadsave import load_pickle, save_pickle

from recon import das, dmas, itdas
from sigproc import iczt
from extras import apply_ant_t_delay
from propspeed import estimate_speed

###############################################################################

# Directory where the time-domain sinograms are located
__DATA_DIR = os.path.join(get_proj_path(), 'data/')

# Directory where the reconstructed images will be stored as .pickle
# files
__OUT_DIR = os.path.join(get_proj_path(), 'output/recon-imgs/')
verify_path(__OUT_DIR)

###############################################################################


def make_recon_pickles(logger=null_logger):
    """Reconstructs images using 4 beamformers, saves images to pickles

    Reconstructs images of all scans in the dataset using the DAS,
    DMAS, itDAS, and itDMAS beamformers. Stores images in a dict, where
    the keys of the dicts are the expt IDs (ex: "c1mf3cm"). Saves
    the dicts to .pickle files.

    Parameters
    ----------
    logger : logging object
        Logger for logging the progress

    """

    # Load the time-domain sinograms
    td_data = load_pickle(os.path.join(__DATA_DIR, 'td_cal_data.pickle'))

    # Load the geometry parameters for each experiment
    geom_params = load_pickle(os.path.join(__DATA_DIR, 'geom_params.pickle'))
    # geom_params = pd.read_csv('metadata/a3_umbmid.csv')

    # Init the dicts for storing the reconstructed images
    das_imgs = dict()
    # dmas_imgs = dict()
    # itdas_imgs = dict()
    # itdmas_imgs = dict()

    for expt_id in td_data.keys():  # For each experiment
    #for expt_id in geom_params.keys():

        # expt_id = '93'
        print("ID: ", expt_id)

        logger.info('\tReconstructing expt id:\t%s' % expt_id)

        # Get the geometry parameters for this scan
        tum_x, tum_y, tum_rad, adi_rad, ant_rad = geom_params[expt_id]
        # print(geom_params[expt_id])
        # geom data is in metres

        # scan 289
        # adi_rad = 0.06 #radius A1
        # ant_rad = 0.21
        ant_rad = apply_ant_t_delay(ant_rad)  # Correct for time delay

        # Estimate average propagation speed for this scan
        speed = estimate_speed(adi_rad=adi_rad, ant_rad=ant_rad)

        # Reconstruct using DAS
        logger.info('\t\tBeginning DAS reconstruction...')

        # fd = fd_data[int(expt_id)]
        # td_data = iczt(fd, ini_t=0, fin_t=6e-9, n_time_pts=700, ini_f=1e9, fin_f=8e9)
        # td_data[expt_id]
        
        das_img = das(td_data[expt_id], ini_t=0, fin_t=6e-9, ant_rad=ant_rad,
                        speed=speed, m_size=500, ini_ant_ang=-130.0)
        das_imgs[expt_id] = das_img

    # Save the image dicts to pickle files
    save_pickle(das_imgs, os.path.join(__OUT_DIR, 'das_imgs.pickle'))
    # save_pickle(dmas_imgs, os.path.join(__OUT_DIR, 'dmas_imgs.pickle'))
    # save_pickle(itdas_imgs, os.path.join(__OUT_DIR, 'itdas_imgs.pickle'))
    # save_pickle(itdmas_imgs, os.path.join(__OUT_DIR, 'itdmas_imgs.pickle'))


###############################################################################


if __name__ == "__main__":

    logger = get_script_logger(__file__)

    logger.info("Beginning...Reconstructing all images...")

    make_recon_pickles(logger=logger)
