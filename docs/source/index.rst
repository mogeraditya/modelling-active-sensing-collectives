Dynamic Model of Cocktail Party Nightmare
==========================================

Agent-based model implementing heuristic behaviours to understand bat collective behaviour.

.. contents:: Table of Contents

Installation of environment
----------------------------

Use the environment_cocktail_3.yml alongside conda in order to install all the pre-requisite packages needed to run these simulations. This can be done by running:

.. code-block:: bash

    conda env create -f environment_cocktail_3.yml

Ensure that the code is run through this environment with the base path set to the repository directory. The base path should be the repository directory and *NOT* the path of individual experiment folders.

.. note:: 
    For more information on setting up the environment, refer to the `environment_cocktail_3.yml` file and the `README.md` in the repository root.

Parameters of the model
-------------------------

For detailed description of the parameters involved in any simulation, please refer to `./dynamic_model/paramsets/description_of_parameters.md`.

.. note:: 
    This file provides an overview of the parameters used in the model. For specific parameter values and configurations, consult the `description_of_parameters.md` file.

How to run the simulation
---------------------------

1. Refer to the `README.md` within the specific experiment folder you want to run.
2. For generic simulation run instructions, refer to `./dynamic_model/README.md`.

.. note:: 
    Experiment-specific instructions can vary, so always check the README in the experiment folder you're working with.

Contact
-------

Reach out to me on `aditya.moger@uni-konstanz.de`.

.. note:: 
    For any questions, feedback, or collaboration opportunities, please don't hesitate to contact me.

.. toctree::
    :maxdepth: 2

    ./dynamic_model/paramsets/description_of_parameters.md
    ./dynamic_model/README.md
    ./README.md
    ./environment_cocktail_3.yml
    ./experiment_folders/ (specific experiment folders)