"""
Módulo de Autenticación
Gestión de usuarios, login, permisos
"""
import hashlib

class AuthManager:
    """Gestor de autenticación"""
    
    def __init__(self):
        self.users = {}
        self.sessions = {}
    
    def register_user(self, username, password, email):
        """Registra nuevo usuario"""
        if not username or len(username) < 3:
            raise ValueError("Username muy corto")
        
        if username in self.users:
            raise ValueError("Usuario ya existe")
        
        if not self._validate_email(email):
            raise ValueError("Email inválido")
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        self.users[username] = {
            'password_hash': password_hash,
            'email': email,
            'active': True
        }
        
        return True
    
    def login(self, username, password):
        """Autentica usuario"""
        if username not in self.users:
            raise ValueError("Usuario no existe")
        
        user = self.users[username]
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if password_hash != user['password_hash']:
            raise ValueError("Password incorrecta")
        
        if not user['active']:
            raise ValueError("Usuario inactivo")
        
        session_id = f"SESSION-{username}-{hash(password)}"
        self.sessions[session_id] = username
        
        return session_id
    
    def logout(self, session_id):
        """Cierra sesión"""
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False
    
    def _validate_email(self, email):
        """Valida formato email"""
        return '@' in email and '.' in email
