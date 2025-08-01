import re
from typing import Tuple

class PatternValidator:
    @staticmethod
    def validate_pattern(pattern: str) -> Tuple[bool, str]:
        if not pattern:
            return False, "Pola tidak boleh kosong"
        
        if len(pattern) < 2:
            return False, "Pola harus minimal 2 karakter"
        
        if len(pattern) > 100:
            return False, "Pola terlalu panjang (maksimal 100 karakter)"
        
        allowed_chars = re.compile(r'^[a-zA-Z0-9\|\\/\-\+\*\.\^\$\(\)\[\]\{\}]+$')
        if not allowed_chars.match(pattern):
            return False, "Pola mengandung karakter yang tidak diizinkan"
        
        return True, "Valid"
    
    @staticmethod
    def suggest_pattern_format(pattern: str) -> str:
        suggestions = []
        
        if len(pattern) < 4:
            suggestions.append("Coba gunakan pola yang lebih panjang untuk hasil yang lebih akurat")
        
        if pattern.count(' ') > 0:
            suggestions.append("Pertimbangkan untuk menggunakan delimiter yang konsisten")
        
        return "; ".join(suggestions) if suggestions else "Pola sudah baik"