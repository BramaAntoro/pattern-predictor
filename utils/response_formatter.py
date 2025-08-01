import json
from datetime import datetime
from typing import Dict, Any

class ResponseFormatter:
    @staticmethod
    def format_prediction_result(result: Dict[str, Any]) -> str:
        if not result.get("success"):
            return f"❌ Error: {result.get('error', 'Unknown error')}"
        
        data = result.get("data", {})
        
        output = f"""
🔍 ANALISIS POLA
================
📥 Input Pola: {data.get('input_pattern', 'N/A')}
🎯 Prediksi Selanjutnya: {data.get('predicted_next', 'N/A')}
📊 Tingkat Kepercayaan: {data.get('confidence', 0)}%
📝 Penjelasan: {data.get('explanation', 'N/A')}
📋 Contoh Pola Lengkap: {data.get('full_pattern_example', 'N/A')}
⏰ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        return output.strip()
    
    @staticmethod
    def save_result_to_json(result: Dict[str, Any], filename: str = "pattern_results.json"):
        try:
            result["timestamp"] = datetime.now().isoformat()
            
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                if not isinstance(existing_data, list):
                    existing_data = [existing_data]
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []
            
            existing_data.append(result)
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Hasil disimpan ke {filename}")
            
        except Exception as e:
            print(f"❌ Error menyimpan file: {e}")
