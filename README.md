# Ceasar salt encryption
# Caesar Cipher con Chiave Segreta + Salt

Un'estensione del classico Caesar Cipher che migliora la sicurezza introducendo una **chiave numerica segreta** e un **salt casuale**.

## 🔐 Cos'è?
- **Caesar Cipher originale**:  
  Ogni lettera del testo in chiaro viene shiftata di un numero fisso di posizioni (es. ROT13 usa shift=13).  
  **Problema**: Facile da decifrare con brute-force (solo 25 possibili shift).

- **Versione migliorata**:  
  - **Chiave segreta**: Un numero (`key`) che determina lo shift base.  
  - **Salt**: Una stringa casuale che modifica dinamicamente lo shift per ogni carattere.  
  - **Risultato**: La cifratura diventa meno prevedibile e più resistente ad attacchi semplici.

## ⚙️ Come Funziona?
1. **Input**:  
   - `plaintext`: Testo da cifrare (es. `"HELLO"`).  
   - `key`: Numero segreto (es. `5`).  
   - `salt`: Stringa casuale (es. `"XQ3"`).  

2. **Processo di cifratura**:  
   - Per ogni carattere in `plaintext`:  
     - Si calcola uno **shift dinamico**:  
       ```
       shift = (key + valore_ASCII_corrente_del_salt) % 26
       ```  
     - Si applica lo shift al carattere (con riavvolgimento alfabetico).  

3. **Esempio**:  
   - `plaintext = "HELLO"`, `key = 5`, `salt = "XQ3"` (valori ASCII: `X=88`, `Q=81`, `3=51`).  
   - Shift calcolati:  
     ```
     H → (5 + 88) % 26 = 15 → W  
     E → (5 + 81) % 26 = 8  → M  
     L → (5 + 51) % 26 = 4  → P  
     L → (5 + 88) % 26 = 15 → A  
     O → (5 + 81) % 26 = 8  → W  
     ```  
   - **Testo cifrato**: `"WMPAW"`.

## 📝 Decifratura
Per decifrare, si usa la formula inversa:  
