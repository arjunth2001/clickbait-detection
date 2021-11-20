# Similarity aware deep attentive model for clickbait detection
Repository of the SMAI Project for Clickbait Detection

## Team Number: 36

## Project Number: 23

## Team Name: (ReLu)ctantly_leaky

## Team Members:

* T. H. Arjun, 2019111012
* Arvindh A, 2019111010
* Thota Gokul Vamsi, 2019111009
* Rakesh Mukkara, 2019101087

## Dataset

* Different versions of the cleaned and the uncleaned dataset which were used can be found [here](https://drive.google.com/drive/folders/1FKXxsgErDDHhljclEJZK1xtAAwYOK6FV?usp=sharing).

## Files and Folders

### data

* This folder contains implementation for creating dataset and cleaning it further.
* Implementation corresponding to generating the dataset can be found in `generate.ipynb`, and cleaning the dataset can be found in `clean.ipynb`.

### baselines

* This folder contains implementation of the baseline corresponding to [this](https://posenhuang.github.io/papers/cikm2013_DSSM_fullversion.pdf) paper - which uses 'Deep Structured Semantic Model' for predicting similarity between a query and a document (used for title and body in our case). This is implemented to validate the performance of approach described in the given paper.
* The complete implementation (pytorch) can be found in `DSSM.ipynb`.
* The outputs (inferences corresponding to train and validation losses) can be found in the `outputs` folder.

### src

* This folder contains the actual implementation of the [given](https://www.researchgate.net/publication/332194860_Similarity-Aware_Deep_Attentive_Model_for_Clickbait_Detection) paper.
* Word2vec was used for obtaining word embeddings. Necessary implementation can be found in `word2vec.ipynb`.
* The implementation corresponding to training of the model can be found in `train.ipynb` and testing can be found in `testing.ipynb`. 
* The outputs (inferences corresponding to train and validation losses) can be found in the `outputs` folder.

## Model Checkpoints

* The saved model checkpoints can be viewed [here](https://iiitaphyd-my.sharepoint.com/:f:/g/personal/arjun_thekoot_research_iiit_ac_in/EpyZblI5sjNLjcuk7lRvbIgBlrAjmJbbrzjmkr8fj4W1Bw?e=YrDpmx).

## References

* Huang, P.S., He, X., Gao, J., Deng, L., Acero, A., Heck, L.: Learning deep structured semantic models for web search using clickthrough data. In: International Conference on Information & Knowledge Management, pp. 2333–2338. ACM (2013)
* Dong, Manqing & Yao, Lina & Wang, Xianzhi & Benatallah, Boualem & Huang, Chaoran. (2019). Similarity-Aware Deep Attentive Model for Clickbait Detection. 