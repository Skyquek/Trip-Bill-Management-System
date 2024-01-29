import 'package:equatable/equatable.dart';

class User extends Equatable {
  final String id;
  final String username;
  final String firstname;
  final String lastname;

  const User(this.id, this.username, this.firstname, this.lastname);

  @override
  List<Object> get props => [id, username, firstname, lastname];

  static const empty = User('-', '-', '-', '-');
}
