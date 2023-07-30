# Millimeter wave drones with cameras: Computer vision aided wireless beam prediction
This is a python code package related to the following article:
Gouranga Charan, Andrew Hredzak, and Ahmed Alkhateeb, "[Millimeter Wave Drones with Cameras: Computer Vision Aided Wireless Beam Prediction](https://arxiv.org/abs/2211.07569)," in 2023 IEEE International Conference on Communications (ICC) Workshop.

# Abstract of the Article
Millimeter wave (mmWave) and terahertz (THz) drones have the potential to enable several futuristic applications such as coverage extension, enhanced security monitoring, and disaster management. However, these drones need to deploy large antenna arrays and use narrow directive beams to maintain a sufficient link budget. The large beam training overhead associated with these arrays makes adjusting these narrow beams challenging for highly-mobile drones. To address these challenges, this paper proposes a vision-aided machine learning-based approach that leverages visual data collected from cameras installed on the drones to enable fast and accurate beam prediction. Further, to facilitate the evaluation of the proposed solution, we build a synthetic drone communication dataset consisting of co-existing wireless and visual data. The proposed vision-aided solution achieves a top-1 beam prediction accuracy of ~91% and close to 100%  top-3 accuracy. These results highlight the efficacy of the proposed solution towards enabling highly mobile mmWave/THz drone communication.

# Code Package Content 
The scripts for generating the results of the ML solutions in the paper. This script adopts ViWi drone scenario.

**To reproduce the results, please follow these steps:**
The Code folder contains the following files and directories:

**Files:**
1. `build_net.py`: Python script for building the DL model.
2. `data_feed.py`: Python script for data feeding and preprocessing.
3. `drone_image_beam_data_BS1.csv`: CSV file containing the BS1 dataset.
4. `drone_image_beam_data_BS1_test.csv`: CSV file containing the test data for the BS1 dataset.
5. `drone_image_beam_data_BS1_train.csv`: CSV file containing the training data for the BS1 dataset.
6. `drone_image_beam_data_BS1_val.csv`: CSV file containing the validation data for the BS1 dataset.
7. `drone_image_beam_data_BS2.csv`: CSV file containing the BS2 dataset.
8. `drone_image_beam_data_BS2_test.csv`: CSV file containing the test data for the BS2 dataset.
9. `drone_image_beam_data_BS2_train.csv`: CSV file containing the training data for the BS2 dataset.
10. `drone_image_beam_data_BS2_val.csv`: CSV file containing the validation data for the BS2 dataset.
11. `main_beam_BS1.py`: Python script for training and saving the checkpoint files for the BS1 dataset.
12. `main_beam_BS2.py`: Python script for training and saving the checkpoint files for the BS2 dataset.
13. `main_beam_eval_BS1.py`: Python script for evaluating the BS1 dataset.
14. `main_beam_eval_BS2.py`: Python script for evaluating the BS2 dataset.
15. `train_val_test_split.py`: Python script for splitting the main CSV files into train, validation, and test CSV files.

**Directories:**
• `saved_folder`: Directory containing the saved checkpoint files for the training sessions.

The `data` folder contains the following directory:
• `images_vision_drones`: Directory containing RGB images related to the dataset.

**Please note that the dataset folder (`images_vision_drones`) is currently located outside of the code folder. To run this code successfully, please move the `images_vision_drones` folder inside the code folder.**

If you have any questions regarding the code and used dataset, please contact [Gouranga Charan](mailto:gcharan@asu.edu?subject=[GitHub]%20ViWi%20drone%20prediction%20implementation).

# License and Referencing
This code package is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). 
If you in any way use this code for research that results in publications, please cite our original article:
> Gouranga Charan, Andrew Hredzak, and Ahmed Alkhateeb, "[Millimeter Wave Drones with Cameras: Computer Vision Aided Wireless Beam Prediction](https://arxiv.org/abs/2211.07569)," arXiv preprint arXiv:2211.07569 (2022).
