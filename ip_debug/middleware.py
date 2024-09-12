import ipaddress
from django.conf import settings

class IPDebugMiddleware:
    """
    Middleware que habilita o deshabilita DEBUG basado en la IP de la solicitud.
    Soporta IPs individuales y rangos de IPs.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = getattr(settings, 'DEBUG_ALLOWED_IPS', [])

    def __call__(self, request):
        #
        # Conseguimos IP del usuario
        ip = request.META.get('REMOTE_ADDR', '')
        
        try:
            client_ip = ipaddress.ip_address(ip)
        except ValueError:
            client_ip = None
        
        # Establecemos estado Debug FALSE
        debug_state = False
        
        # Si IP Corresponde a las permitidas, DEBUG TRUE
        if any(self.is_ip_allowed(client_ip, allowed_ip) for allowed_ip in self.allowed_ips):
            settings.DEBUG = True
            debug_state = True
        
        # Intentamos informar al log Django del acceso a DEBUG
        if settings.DEBUG != debug_state:
            try:
                logger.info(f"DEBUG set to {debug_state} for IP {ip}")
            except:
                pass
        
        response = self.get_response(request)
        return response

    def is_ip_allowed(self, client_ip, allowed_ip):
        """
        Verifica si la IP del cliente está dentro del rango o es exacta.
        """
        try:
            allowed_network = ipaddress.ip_network(allowed_ip, strict=False)
            return client_ip in allowed_network
        except ValueError:
            return False
