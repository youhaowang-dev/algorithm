# Array, Hash Table, String
# Twitch 12 Amazon 2 Intuit 5 Microsoft 2 Google Wix
# https://leetcode.com/problems/unique-email-addresses/

# Every valid email consists of a local name and a domain name, separated by the '@' sign.
# Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address,
# mail sent there will be forwarded to the same address without dots in the local name.
# Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
# This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

# Example 1:
# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
# Example 2:
# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3

from ast import List

# time O(m*n) where m is email count and n is the average email length
# space O(m*n) worst case is all emails are unique, so all emails are saved in set
class UniqueEmailAddresses:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails:
            return 0

        unique_emails = set()
        for email in emails:
            name, domain = email.split("@")
            name_first_part = name.split("+")[0]
            parsed_name = name_first_part.replace(".", "")
            # @ is needed for a@bc and ab@c
            unique_emails.add(parsed_name + "@" + domain)

        return len(unique_emails)
