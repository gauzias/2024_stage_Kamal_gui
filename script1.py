import os
import re
import time
import numpy as np
import pandas as pd
import nibabel as nib
import ants
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
import tools as tls

if __name__ == "__main__":
    debut = time.time()

    nom_general_sujet = r'^sub-00\d+\_ses-00\d+\_acq-haste_rec-nesvor_desc-aligned_T2w.nii.gz'
    nom_general_sujet_rot = r'^sub-00\d+\_ses-00\d+\_acq-haste_rec-nesvor_desc-aligned_T2w_rot.nii.gz'
    all_sujets_path = "/envau/work/meca/users/2024_Kamal/real_data/lastest_nesvor/"
    path_ouput = "/envau/work/meca/users/2024_Kamal/output/output_script1"
    Nom_caract = r'^STA\d+\.nii.gz'
    path_des_atlas = "/envau/work/meca/users/2024_Kamal/Sym_Hemi_atlas/Fetal_atlas_gholipour/T2"

    files_atlas = tls.Parcours_dossier_only_data_match(path_des_atlas, Nom_caract)
    tab_path_sujet = tls.recup_sujet(all_sujets_path, nom_general_sujet)
    list_path_sujet_rot = [tls.creation_PATH_pour_fichier_swaper(sujet_path, path_ouput) for sujet_path in tab_path_sujet]
    for path_sujet_rot,path_sujet in zip(list_path_sujet_rot, tab_path_sujet):
        tls.SWAP_COPY_INFO_SAVE(path_sujet,path_sujet_rot)

    tab_path_sujet_rot = tls.recup_sujet(all_sujets_path, nom_general_sujet_rot)
    print(list_path_sujet_rot)
    tab_repertoire, tab_img_sujet = tls.path_abs_sujet_to_fichier_repertorie_sujet(list_path_sujet_rot)
    criteres = ['MattesMutualInformation']


    List_atlas_finaux = []
    for sujet, repertoire in zip(tab_img_sujet, tab_repertoire):
        tab2D_global, Bon_atlas = tls.recupAtlas_to_tableau_simil(files_atlas, criteres, path_des_atlas, sujet, repertoire, "Rigid", "linear")
        print(tab2D_global)
        List_atlas_finaux.append(Bon_atlas )
        print(f"l'atlas qui maximise l'information mutuel est : {Bon_atlas} pour {sujet}\n")


    tableau_bon_atlas_by_sujet = [(tab_img_sujet), (List_atlas_finaux)]
    print(tableau_bon_atlas_by_sujet)

