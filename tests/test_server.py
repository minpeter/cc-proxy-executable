def test_server_startup():
    from server import Server
    server = Server()
    assert server is not None