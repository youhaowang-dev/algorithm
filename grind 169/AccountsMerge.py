# Array, String, Depth-First Search, Breadth-First Search, Union Find
# https://leetcode.com/problems/accounts-merge/description/
# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0]
# is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some
# common email to both accounts. Note that even if two accounts have the same name, they may belong to different
# people as people could have the same name. A person can have any number of accounts initially, but all of their
# accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the
# name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Example 1:
# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
class AccountsMerge:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        connects = dict()  # undirected graph, email to connected emails

        for acc in accounts:
            for i in range(2, len(acc)):  # emails in the same list are connected
                email1 = acc[i]
                email2 = acc[i-1]
                if email1 not in connects:
                    connects[email1] = list()
                if email2 not in connects:
                    connects[email2] = list()

                connects[email1].append(email2)
                connects[email2].append(email1)

        merged = list()
        seen = set()
        for acc in accounts:
            first_email = acc[1]
            if first_email not in seen:
                connected_emails = self.get_connected_emails(
                    first_email, connects, seen)
                merged.append([acc[0]] + sorted(connected_emails))

        return merged

    def get_connected_emails(self, email, connects, seen):
        seen.add(email)
        emails = list()
        emails.append(email)
        # email may not in dict
        for connected_email in connects.get(email, list()):
            if connected_email not in seen:
                emails.extend(self.get_connected_emails(
                    connected_email, connects, seen))

        return emails
