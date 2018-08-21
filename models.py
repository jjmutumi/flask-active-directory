import ldap3

def authenticate(server_uri, domain, username, password):
    user_dc = ["cn=" + username] + ["dc=" + dc for dc in domain.split(".")]
    user_dc = ",".join(user_dc)
    server = ldap3.Server(server_uri, get_info=ldap3.ALL)
    connection = ldap3.Connection(server, user=user_dc, password=password)

    if not connection.bind():
		raise ValueError("Invalid credentials")