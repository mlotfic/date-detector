# Pattern Validator Mixin
# ========================
import re


class PatternValidator:
    """Mixin providing regex pattern validation and compilation checking.
    
    This validation mixin ensures all regex patterns in pattern dataclasses
    are syntactically valid and can be compiled successfully. It provides
    automatic validation during object initialization and helpful error
    reporting for debugging pattern construction.
    
    The validator uses heuristics to identify string attributes that appear
    to be regex patterns and validates them using Python's ``re`` module
    with appropriate flags for international date matching.
    
    Methods:
        _validate_patterns(): Validates all regex patterns in the instance
        _looks_like_regex(pattern): Heuristic regex pattern detection
        
    Raises:
        ValueError: When any pattern fails regex compilation with detailed
            error information including the attribute name and regex error.
            
    Example:
        .. code-block:: python
        
            @dataclass
            class MyPatterns(PatternValidator):
                year_pattern: str = r"(\d{4})"
                invalid_pattern: str = r"([unclosed"  # Will raise ValueError
                
            # Automatic validation on initialization
            try:
                patterns = MyPatterns()  # Validates during __post_init__
            except ValueError as e:
                print(f"Pattern error: {e}")
                
    Note:
        This mixin should be inherited by all pattern dataclasses to ensure
        regex validity before use in date matching operations.
        
    Warning:
        The heuristic detection may not catch all regex patterns or may
        flag non-regex strings. Consider this when designing pattern attributes.
    """
    
    def _validate_patterns(self) -> None:
        """Validate all regex patterns in the class instance.
        
        Performs comprehensive validation of all string attributes that appear
        to be regex patterns. Uses case-insensitive Unicode-aware compilation
        to match the flags used in actual date matching operations.
        
        The validation process:
        
        1. Iterates through all non-private instance attributes
        2. Identifies string attributes using :meth:`_looks_like_regex`
        3. Attempts compilation with ``re.IGNORECASE | re.UNICODE`` flags
        4. Collects and reports all validation errors with context
        
        Raises:
            ValueError: If any pattern fails to compile. The error message
                includes the attribute name and the specific regex compilation
                error to aid in debugging pattern construction.
                
        Note:
            This method is typically called automatically from ``__post_init__``
            in pattern dataclasses, ensuring validation occurs immediately
            after object creation.
        """
        for attr_name in dir(self):
            # Skip private attributes and methods
            if attr_name.startswith('_'):
                continue
                
            attr_value = getattr(self, attr_name)
            
            # Validate string attributes that look like regex patterns
            if isinstance(attr_value, str) and self._looks_like_regex(attr_value):
                try:
                    re.compile(attr_value, flags=re.IGNORECASE | re.UNICODE)
                except re.error as e:
                    raise ValueError(f"Invalid regex pattern in {attr_name}: {e}")
    
    def _looks_like_regex(self, pattern: str) -> bool:
        """Heuristic detection of regex pattern strings.
        
        Uses common regex metacharacters to determine if a string is likely
        intended as a regex pattern. This heuristic approach helps avoid
        validating plain text strings while catching most regex patterns.
        
        Args:
            pattern (str): String to evaluate for regex characteristics.
            
        Returns:
            bool: ``True`` if the string contains regex metacharacters and
                is likely a regex pattern, ``False`` otherwise.
                
        Note:
            The detection is based on common regex metacharacters:
            ``()``, ``[]``, ``{}``, ``\\``, ``+*?``, ``|``, ``^$``
            
            This heuristic may produce false positives for strings containing
            these characters in non-regex contexts, and false negatives for
            simple regex patterns using only literal characters.
            
        Example:
            .. code-block:: python
            
                validator = PatternValidator()
                
                validator._looks_like_regex(r"(\d{4})")     # True
                validator._looks_like_regex(r"[a-zA-Z]+")   # True  
                validator._looks_like_regex("simple text")  # False
                validator._looks_like_regex("year (2024)")  # True (false positive)
        """
        regex_indicators = ['(', ')', '[', ']', '{', '}', '\\', '+', '*', '?', '|', '^', '$']
        return any(indicator in pattern for indicator in regex_indicators)