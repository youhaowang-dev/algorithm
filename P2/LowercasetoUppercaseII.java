// Implement an upper method to convert all characters in a string to uppercase.
// The characters not in alphabet don't need to convert.

class LowercasetoUppercaseII {

  public String lowercaseToUppercase2(String letters) {
    StringBuilder converted = new StringBuilder();
    for (char character : letters.toCharArray()) {
      if (Character.isLowerCase(character)) {
        converted.append(Character.toUpperCase(character));
      } else {
        converted.append(character);
      }
    }

    return converted.toString();
  }
}
