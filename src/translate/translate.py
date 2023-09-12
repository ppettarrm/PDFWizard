from googletrans import Translator
from extract import extractText
from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, src_lang, tgt_lang):
    try:
        model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
        try:
            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)
        except:
            # If the model for the specified language pair is not found, use google translate as a fallback
            translator = Translator()
            translated = translator.translate(text, src=src_lang, dest=tgt_lang)
            return translated.text

        sentences = text.split('. ')
        translated_sentences = []

        for sentence in sentences:
            inputs = tokenizer(sentence, return_tensors="pt", padding=True)
            translated = model.generate(**inputs)
            tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
            translated_sentences.append(tgt_text[0])

        # Join the translated sentences to form the translated text
        translated_text = '. '.join(translated_sentences)
        translated_text = translated_text.replace('..', '.')

        return translated_text
    except Exception as e:
        return f"An error occurred during translation: {e}"

def translate_pdf():
    try:
        input_path = input("Enter the path to the PDF file: ")
        output_path = input("Enter the path to save the translated PDF (include file name and .txt extension): ")
        source_language = input("Enter the source language code (e.g., 'en' for English): ")
        target_language = input("Enter the target language code (e.g., 'sr' for Serbian): ")

        text = extractText.extract_text(input_path)

        translated_text = translate_text(text, source_language, target_language)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated_text)

        print(f"The translated text has been saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
