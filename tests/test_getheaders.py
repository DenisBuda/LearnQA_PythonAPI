import requests

class TestGetMyHeaders:
    def setup(self):
        self.etalon_content_type = "application/json"
        self.etalon_content_length = "15"
        self.etalon_connection = "keep-alive"
        self.etalon_keep_alive = "timeout=10"
        self.etalon_server = "Apache"
        self.etalon_secret_header = "Some secret value"
        self.etalon_cache_control = "max-age=0"

    def test_get_headers(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        # print(response.headers)
        my_content_type_header = response.headers.get("Content-Type")
        my_content_length_header = response.headers.get("Content-Length")
        my_content_connection_header = response.headers.get("Connection")
        my_keep_alive = response.headers.get("Keep-Alive")
        my_server = response.headers.get("Server")
        my_secret_header = response.headers.get("x-secret-homework-header")
        my_cache_control = response.headers.get("Cache-Control")
        my_date = response.headers.get("Date")
        my_expires = response.headers.get("Expires")

        print("All values from response headers:")
        print(my_content_type_header)
        print(my_content_length_header)
        print(my_content_connection_header)
        print(my_keep_alive)
        print(my_server)
        print(my_secret_header)
        print(my_cache_control)
        print(my_date)
        print(my_expires)

        assert my_date == my_expires, "Error! Date is not equal to Expire"
        assert my_content_type_header == self.etalon_content_type, "Error! Invalid Content-Type"
        assert my_content_length_header == self.etalon_content_length, "Error! Invalid Content-Length"
        assert my_content_connection_header == self.etalon_connection, "Error! Invalid Connection"
        assert my_keep_alive == self.etalon_keep_alive, "Error! Invalid Keep-Alive"
        assert my_server == self.etalon_server, "Error! Invalid Server"
        assert my_secret_header == self.etalon_secret_header, "Error! Invalid x-secret-homework-header"
        assert my_cache_control == self.etalon_cache_control, "Error! Invalid Cache-Control"