import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
from typing import Optional, Dict, Any

load_dotenv()

class GeminiPatternAPI:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY tidak ditemukan dalam environment variables")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')   
    def predict_pattern(self, pattern: str) -> Dict[str, Any]:

        prompt = f"""
        Analisis pola berikut dan prediksi elemen selanjutnya:
        
        Pola: {pattern}
        
        Tugas:
        1. Identifikasi pola yang berulang
        2. Berikan prediksi elemen/karakter selanjutnya
        3. Jelaskan logika di balik pola tersebut
        4. Berikan tingkat kepercayaan prediksi (1-100%)
        
        Format response dalam JSON:
        {{
            "input_pattern": "{pattern}",
            "predicted_next": "prediksi_elemen_selanjutnya",
            "explanation": "penjelasan_logika_pola",
            "confidence": tingkat_kepercayaan_angka,
            "full_pattern_example": "contoh_pola_lengkap_dengan_prediksi"
        }}
        
        Contoh:
        - Jika pola "//|//|" maka prediksi selanjutnya adalah "//"
        - Jika pola "ABC ABC" maka prediksi selanjutnya adalah "ABC"
        """
        
        try:
            response = self.model.generate_content(prompt)
            
            response_text = response.text.strip()
            
            try:
                start_idx = response_text.find('{')
                end_idx = response_text.rfind('}') + 1
                
                if start_idx != -1 and end_idx != -1:
                    json_str = response_text[start_idx:end_idx]
                    result = json.loads(json_str)
                else:
                    result = {
                        "input_pattern": pattern,
                        "predicted_next": "Tidak dapat diprediksi",
                        "explanation": response_text,
                        "confidence": 0,
                        "full_pattern_example": pattern + "?"
                    }
                    
            except json.JSONDecodeError:
                result = {
                    "input_pattern": pattern,
                    "predicted_next": "Parsing error",
                    "explanation": response_text,
                    "confidence": 0,
                    "full_pattern_example": pattern + "?"
                }
            
            return {
                "success": True,
                "data": result,
                "raw_response": response_text
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "data": None
            }
    
    def analyze_multiple_patterns(self, patterns: list) -> Dict[str, Any]:
       
        results = []
        
        for pattern in patterns:
            result = self.predict_pattern(pattern)
            results.append(result)
        
        return {
            "total_patterns": len(patterns),
            "results": results
        }