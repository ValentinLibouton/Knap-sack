# Knapsack Models in Python

Ce dépôt contient une collection de scripts Python pour formuler et résoudre différentes variantes du problème du sac à dos (0/1, non borné, relaxations LP) à l’aide de PuLP et/ou GLPK.

---

## 📂 Contenu

- `six_knapsack_models.py`  
  Implémente et résout les 6 modèles suivants avec PuLP :  
  1. **maxKP 0/1** (sac unique, variables binaires)  
  2. **minKP 0/1** (sac unique, variables binaires)  
  3. **maxKP int** (unbounded knapsack, variables entières ≥ 0)  
  4. **minKP int** (unbounded, variables entières ≥ 0)  
  5. **maxKP LP** (relaxation continue de 0/1)  
  6. **minKP LP** (relaxation continue de 0/1)  

- `README.md`  
  Ce document.

- (Optionnel) Modèles GMPL (`.mod`) et fichiers de données (`.dat`)  
  Pour qui préfère GLPK en ligne de commande.

---

## ⚙️ Prérequis

- **Python 3.7+**  
- **pip**  
- **GLPK** (optionnel, pour utiliser directement `glpsol`)  
  - Sous Debian/Ubuntu :  
    ```bash
    sudo apt update
    sudo apt install -y glpsol libglpk-dev
    ```  
  - Sous macOS via Homebrew :  
    ```bash
    brew install glpk
    ```  
  - Sous Windows :  
    Téléchargez Winglpk et ajoutez `...\glpk\bin` à votre `PATH`.

- **Packages Python**  
  ```bash
  pip install pulp        # Interface Python haut‑niveau pour LP/MIP
  pip install swiglpk     # (si vous voulez piloter GLPK directement)
  ```

