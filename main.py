import sys
import os
from api.gemini_api import GeminiPatternAPI
from utils.pattern_validator import PatternValidator
from utils.response_formatter import ResponseFormatter

def main():
    print("🤖 APLIKASI PENEBAKAN POLA DENGAN GEMINI AI")
    print("=" * 50)
    
    try:
        gemini_api = GeminiPatternAPI()
        validator = PatternValidator()
        formatter = ResponseFormatter()
        
        while True:
            print("\n📝 Menu:")
            print("1. Prediksi pola tunggal")
            print("2. Prediksi multiple pola")
            print("3. Keluar")
            
            choice = input("\nPilih menu (1-3): ").strip()
            
            if choice == '1':
                pattern = input("\n🔤 Masukkan pola (contoh: //|//|): ").strip()
                
                is_valid, message = validator.validate_pattern(pattern)
                if not is_valid:
                    print(f"❌ {message}")
                    continue
                
                print("\n🔄 Menganalisis pola...")
                result = gemini_api.predict_pattern(pattern)
                
                formatted_result = formatter.format_prediction_result(result)
                print(formatted_result)
                
                save_choice = input("\n💾 Simpan hasil ke JSON? (y/n): ").strip().lower()
                if save_choice == 'y':
                    formatter.save_result_to_json(result)
                
            elif choice == '2':
                print("\n🔤 Masukkan beberapa pola (pisahkan dengan koma):")
                patterns_input = input("Contoh: //|//|, ABC ABC, 123 123: ").strip()
                
                patterns = [p.strip() for p in patterns_input.split(',') if p.strip()]
                
                if not patterns:
                    print("❌ Tidak ada pola yang valid")
                    continue
                
                valid_patterns = []
                for pattern in patterns:
                    is_valid, message = validator.validate_pattern(pattern)
                    if is_valid:
                        valid_patterns.append(pattern)
                    else:
                        print(f"❌ Pola '{pattern}' tidak valid: {message}")
                
                if not valid_patterns:
                    print("❌ Tidak ada pola yang valid untuk diproses")
                    continue
                
                print(f"\n🔄 Menganalisis {len(valid_patterns)} pola...")
                results = gemini_api.analyze_multiple_patterns(valid_patterns)
                
                print(f"\n📊 HASIL ANALISIS {len(valid_patterns)} POLA")
                print("=" * 50)
                
                for i, result in enumerate(results['results'], 1):
                    print(f"\n--- Pola {i} ---")
                    formatted_result = formatter.format_prediction_result(result)
                    print(formatted_result)
                
                save_choice = input("\n💾 Simpan semua hasil ke JSON? (y/n): ").strip().lower()
                if save_choice == 'y':
                    formatter.save_result_to_json(results, "multiple_pattern_results.json")
                
            elif choice == '3':
                print("\n👋 Terima kasih telah menggunakan aplikasi ini!")
                break
                
            else:
                print("❌ Pilihan tidak valid")
    
    except KeyboardInterrupt:
        print("\n\n👋 Aplikasi dihentikan oleh user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("💡 Pastikan API Key Gemini sudah benar dan koneksi internet stabil")

if __name__ == "__main__":
    main()