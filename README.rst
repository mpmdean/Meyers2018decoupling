==========================================================
Data Repository
==========================================================
Source code and data files for the manuscript Electronic character of charge order in square planar low valence nickelates. Execute plot.ipynb to view the data.

How to cite
-----------
If this data is used, please cite ``Decoupling carrier concentration and electron-phonon coupling in oxide heterostructures observed with resonant inelastic x-ray scattering'', Derek Meyers, Ken Nakatsukasa, Sai Mu, Lin Hao, Junyi Yang, Yue Cao, G Fabbris, Hu Miao, J Pelliciari, D McNally, M. Dantz, E. Paris, E. Karapetrova, Yongseong Choi, D. Haskel, P. Shafer, E. Arenholz, Thorsten Schmitt, Tom Berlijn, S. Johnston, Jian Liu, and M. P. M. Dean
Phys. Rev. Lett. 121, 236802 (2018)


Run locally
-----------

Work with this by installing `docker <https://www.docker.com/>`_ and pip and then running

.. code-block:: bash

       pip install jupyter-repo2docker
       jupyter-repo2docker --editable .

Change `tree` to `lab` in the URL for JupyterLab.

Run remotely
------------

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/mpmdean/Shen2022character/HEAD?filepath=plot.ipynb
