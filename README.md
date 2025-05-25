# flower-classifier

## Project Description
This project classifies different flower varieties.

### Name & URL
| Name          | URL |
|---------------|-----|
| Huggingface   | [Huggingface Space](https://huggingface.co/spaces/lautenad/flower-classifier) |
| Model Page    | [Huggingface Model Page](https://huggingface.co/spaces/lautenad/flower-classifier) |
| Code          | [GitHub Repository](https://github.com/lautenad/flower-classifier) |

## Labels
The different breeds are:  
`["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", 
    "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood",
    "globe thistle", "snapdragon", "colt's foot", "king protea", "spear thistle", 
    "yellow iris", "globe-flower", "purple coneflower", "peruvian lily", "balloon flower",
    "giant white arum lily", "fire lily", "pincushion flower", "fritillary", 
    "red ginger", "grape hyacinth", "corn poppy", "prince of wales feathers", 
    "stemless gentian", "artichoke", "sweet william", "carnation", "garden phlox",
    "love in the mist", "mexican aster", "alpine sea holly", "ruby-lipped cattleya",
    "cape flower", "great masterwort", "siam tulip", "lenten rose", "barbeton daisy",
    "daffodil", "sword lily", "poinsettia", "bolero deep blue", "wallflower", 
    "marigold", "buttercup", "oxeye daisy", "common dandelion", "petunia", "wild pansy",
    "primula", "sunflower", "pelargonium", "bishop of llandaff", "gaura", "geranium",
    "orange dahlia", "pink-yellow dahlia?", "cautleya spicata", "japanese anemone",
    "black-eyed susan", "silverbush", "californian poppy", "osteospermum", "spring crocus",
    "bearded iris", "windflower", "tree poppy", "gazania", "azalea", "water lily", 
    "rose", "thorn apple", "morning glory", "passion flower", "lotus", "toad lily", 
    "anthurium", "frangipani", "clematis", "hibiscus", "columbine", "desert-rose", 
    "tree mallow", "magnolia", "cyclamen", "watercress", "canna lily", "hippeastrum", 
    "bee balm", "ball moss", "foxglove", "bougainvillea", "camellia", "mallow", 
    "mexican petunia", "bromelia", "blanket flower", "trumpet creeper", "blackberry lily", 
    "common tulip", "wild rose"]`

## Data Sources and Features Used Per Source
| Data Source | Description |
|-------------|-------------|
| [Oxford-Flower](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/) | Original dataset from Oxford containing 102 varieties of flowers. |

## Model Training

### Data Splitting Method (Train/Validation/Test)

The model was trained on the **Oxford Flowers 102** dataset, which contains 8189 images across 102 different flower categories.  
Since the original dataset does not include validation or test splits, they were created manually:

| Split      | Number of Images |
|------------|------------------:|
| Train      | 6551              |
| Validation | 819               |
| Test       | 819               |

---

### Training Details

The model was fine-tuned using a pre-trained **Vision Transformer (ViT)**  
[`google/vit-base-patch16-224`](https://huggingface.co/google/vit-base-patch16-224).

**Training configuration:**

- **Learning rate:** `3e-4`  
- **Batch size:** `16`  
- **Epochs:** `5`  
- **Model:** `ViTForImageClassification`  
- **Frameworks:** Hugging Face Transformers & Datasets  
- **Training API:** `Trainer`  
- **Model hosted on Hugging Face Hub:** [`lautenad/vit-base-flowers102`](https://huggingface.co/lautenad/vit-base-flowers102)

---

### Training Progress

| Epoch | Training Loss | Validation Accuracy |
|-------|----------------|----------------------|
| 1     | 1.254          | 77.18 %              |
| 2     | 0.941          | 83.51 %              |
| 3     | 0.835          | 84.59 %              |
| 4     | 0.758          | 86.08 %              |
| 5     | 0.702          | 86.55 %              |


### TensorBoard

Details of training can be found at [Huggingface TensorBoard](https://huggingface.co/kuhs/vit-base-oxford-iiit-pets/tensorboard)

| Model/Method                                                         | TensorBoard Link                                      |
|----------------------------------------------------------------------|------------------------------------------------------|
| Transfer Learning with `google/vit-base-patch16-224` (without data augmentation) | runs/Feb07_17-31-08_clt-mob-w-2019                    |
| Transfer Learning with `google/vit-base-patch16-224` (with data augmentation)  | runs/Feb07_17-09-30_clt-mob-w-2019                    |

![alt text](doc/eval.png)


## Results
| Model/Method                                                         | Accuracy | Precision | Recall |
|----------------------------------------------------------------------|----------|-----------|--------|
| Transfer Learning with `google/vit-base-patch16-224` (without data augmentation) | 93%      | -         | -      |
| Transfer Learning with `google/vit-base-patch16-224` (with data augmentation)  | 95%      | -         | -      |
| Zero-shot Image Classification with `openai/clip-vit-large-patch14` | 88%      | 87.68%    | 88%    |

## References
![Class Distribution](doc/class_distribution.png)  
![Dog vs Cat](doc/dog_cat.png)  
![Sample Prediction (Transfer Learning)](doc/sample_prediction_transferlearning.png)
