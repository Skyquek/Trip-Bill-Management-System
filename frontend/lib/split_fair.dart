import 'package:bill_splitter/src/modules/login/view/login_form.dart';
import 'package:dio/dio.dart';
import 'package:flutter/material.dart';

class SplitFair extends StatelessWidget {
  const SplitFair({super.key});

  void loginUser() async {
    const username = 'user1';
    const email = 'user1@example.com';
    const password = 'password!!';

    const endpoint = 'http://localhost:8000/dj-rest-auth/login/';

    final dio = Dio();

    try {
      final response = await dio.post(endpoint, data: {
        'username': username,
        'email': email,
        'password': password,
      });

      print(response.data);
    } catch (e) {
      print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: LoginForm(),
    );
  }
}
