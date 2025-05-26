import gradio as gr
from transformers import pipeline

# Lade Modelle
vit_classifier = pipeline("image-classification", model="lautenad/vit-base-flowers102")
clip_detector = pipeline(model="openai/clip-vit-large-patch14", task="zero-shot-image-classification")

# Labels (Flowers102)
labels_flowers102 = [
    "pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", 
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
    "common tulip", "wild rose"
]

# Klassifizierungsfunktion
def classify_flower(image):
    vit_results = vit_classifier(image)
    vit_output = {}
    for r in vit_results:
        try:
            idx = int(r["label"].replace("LABEL_", "")) if isinstance(r["label"], str) else int(r["label"])
            label = labels_flowers102[idx]
        except:
            label = str(r["label"])
        vit_output[label] = float(r["score"])

    clip_results = clip_detector(image, candidate_labels=labels_flowers102)
    clip_output = {r["label"]: float(r["score"]) for r in clip_results}

    return {
        "ViT Classification": vit_output,
        "CLIP Zero-Shot Classification": clip_output
    }

# Beispielbilder (Pfadangabe relativ zum Projekt-Root in Hugging Face!)
example_images = [
    ["example-images/camellia.jpg"],
    ["example-images/mallow.jpg"],
    ["example-images/rose.jpg"],
    ["example-images/Tiger-lily.jpg"],
    ["example-images/wallflower.jpg"]
]

# Gradio UI
iface = gr.Interface(
    fn=classify_flower,
    inputs=gr.Image(type="pil"),
    outputs=gr.JSON(),
    title="Flower Classification Comparison",
    description="Upload an image of a flower and compare ViT vs CLIP results.",
    examples=example_images
)

iface.launch()
