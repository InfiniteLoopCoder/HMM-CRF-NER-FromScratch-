from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")

sorted_labels_eng= ["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "B-MISC" , "I-MISC"]

sorted_labels_chn = [
'O',
'B-NAME', 'M-NAME', 'E-NAME', 'S-NAME'
, 'B-CONT', 'M-CONT', 'E-CONT', 'S-CONT'
, 'B-EDU', 'M-EDU', 'E-EDU', 'S-EDU'
, 'B-TITLE', 'M-TITLE', 'E-TITLE', 'S-TITLE'
, 'B-ORG', 'M-ORG', 'E-ORG', 'S-ORG'
, 'B-RACE', 'M-RACE', 'E-RACE', 'S-RACE'
, 'B-PRO', 'M-PRO', 'E-PRO', 'S-PRO'
, 'B-LOC', 'M-LOC', 'E-LOC', 'S-LOC'
]

def check(language, gold_path, my_path):
    if language == "English":
        sort_labels = sorted_labels_eng
    else:
        sort_labels = sorted_labels_chn
    y_true = []
    y_pred = []
    with open(gold_path, "r") as g_f, open(my_path, "r") as m_f:
        g_lines = g_f.readlines()
        m_lines = m_f.readlines()

        #assert len(g_lines) == len(m_lines), "Length is Not Equal."
        for i in range(len(g_lines)):
            if g_lines[i] == "\n":
                continue
            g_word, g_tag = g_lines[i].strip().split(" ")
            m_word, m_tag = m_lines[i].strip().split(" ")
            y_true.append(g_tag)
            y_pred.append(m_tag)
    print(metrics.classification_report(
        y_true = y_true, y_pred=y_pred, labels=sort_labels[1:], digits=4
    ))
    return

if __name__ == "__main__":
    model = input("Model (1/2/3): ")
    while model not in ['1', '2', '3']:
        print("Invalid model. Please choose 1, 2, 3.")
        model = input("Model (1/2/3): ")

    dataset = input("Dataset (t->train/v->validation/test): ")
    while dataset not in ['t', 'v', 'test']:
        print("Invalid dataset. Please choose t, v or test.")
        dataset = input("Dataset (t->train/v->validation/test): ")
    
    if dataset == 't':
        dataset = 'train'
    elif dataset == 'v':
        dataset = 'validation'

    language = input("Language (e->English/c->Chinese): ")
    while language not in ['e', 'c']:
        print("Invalid language. Please choose e or c.")
        language = input("Language (e->English/c->Chinese): ")
    
    if language == 'e':
        language = 'English'
    else:
        language = 'Chinese'

    print(f"--------------------------------Test Model {model}--------------------------------")
    print(f"{language} {dataset.title()} Set:")
    check(language=language,
          gold_path=f"{language}/{dataset}.txt", 
          my_path=f"{language}/{dataset}_{model}.txt")
