# Pdf2QuizBuilder

Pdf2QuizBuilder è uno strumento desktop in Python che ti permette di selezionare graficamente sezioni di un PDF contenenti domande e salvarle in un file JSON strutturato, insieme alle risposte corrette e all'immagine ritagliata della domanda.

## ✨ Caratteristiche
- Interfaccia grafica interattiva (Tkinter)
- Navigazione tra pagine del PDF
- Selezione tramite riquadro di aree con le domande
- Inserimento della risposta corretta
- Salvataggio automatico in `output.json` con:
  - ID domanda
  - Numero di pagina
  - Coordinate del riquadro
  - Risposta corretta
  - Percorso immagine ritagliata

## 📦 Requisiti

- Python 3.x
- tkinter
- Pillow
- PyMuPDF (`fitz`)

Installa le dipendenze con:
```bash
pip install PyMuPDF pillow
