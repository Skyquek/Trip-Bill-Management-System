import 'package:authentication_api/authentication_api.dart';
import 'package:dio/dio.dart';

class DjangoUserAuthApi extends AuthenticationApi<Future<String>> {
  final endpoint = 'http://localhost:8000/dj-rest-auth/';

  @override
  Future<String> logIn(
      {required String username, required String password}) async {
    const username = 'user1';
    const email = 'user1@example.com';
    const password = 'password!!';

    final dio = Dio();

    try {
      final response = await dio.post('${endpoint}login/', data: {
        'username': username,
        'email': email,
        'password': password,
      });

      final apiKey = response.data['key'];

      return apiKey;
    } catch (e) {
      print(e);
      return e.toString();
    }
  }

  @override
  void logOut() async {
    final dio = Dio();
    try {
      final response = await dio.post('${endpoint}logout/');

      print(response.data);
    } catch (e) {
      print(e);
    }
  }
}
