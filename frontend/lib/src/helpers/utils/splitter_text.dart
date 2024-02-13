import 'package:flutter/material.dart';

class SplitterText extends StatelessWidget {
  final String text;
  final int? fontWeight;

  SplitterText(this.text, {this.fontWeight});
  SplitterText.displaySmall(
    this.text, {
    this.fontWeight,
  });

  @override
  Widget build(BuildContext context) {
    // TODO(Quek): Allow users to add textstyle
    return Text(text);
  }
}
