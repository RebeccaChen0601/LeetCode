/*
 * @lc app=leetcode id=720 lang=java
 *
 * [720] Longest Word in Dictionary
 *
 * https://leetcode.com/problems/longest-word-in-dictionary/description/
 *
 * algorithms
 * Easy (44.08%)
 * Total Accepted:    32.2K
 * Total Submissions: 73.1K
 * Testcase Example:  '["w","wo","wor","worl","world"]'
 *
 * Given a list of strings words representing an English Dictionary, find the
 * longest word in words that can be built one character at a time by other
 * words in words.  If there is more than one possible answer, return the
 * longest word with the smallest lexicographical order.  If there is no
 * answer, return the empty string.
 * 
 * Example 1:
 * 
 * Input: 
 * words = ["w","wo","wor","worl", "world"]
 * Output: "world"
 * Explanation: 
 * The word "world" can be built one character at a time by "w", "wo", "wor",
 * and "worl".
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: 
 * words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
 * Output: "apple"
 * Explanation: 
 * Both "apply" and "apple" can be built from other words in the dictionary.
 * However, "apple" is lexicographically smaller than "apply".
 * 
 * 
 * 
 * Note:
 * All the strings in the input will only contain lowercase letters.
 * The length of words will be in the range [1, 1000].
 * The length of words[i] will be in the range [1, 30].
 * 
 */
class Solution {
    public String longestWord(String[] words) {
        Trie trie = new Trie();
        int index = 0;
        for(String word : words) {
            trie.insert(word, ++index);
        }
        return trie.findWord(words, trie);
    }
}

class Node{
    HashMap <Character, Node> map = new HashMap <Character, Node>();
    char c;
    int index;
    Node(char c){
        this.c = c;
    }
}

class Trie{
    Node root;
    
    Trie(){
        root = new Node('0');
    }
    
    void insert(String word, int index) {
        Node curr = root;
        for(char c : word.toCharArray()){
            curr.map.putIfAbsent(c, new Node(c));
            curr = curr.map.get(c);
        }
        curr.index = index;
    }

    String findWord(String[]words, Trie trie) {
        int longest, length = 0;
        String ans = "";
        Node curr = trie.root;
        Stack<Node> stack = new Stack<Node>();
        stack.push(curr);
        while(!stack.empty()) {
            Node node = stack.pop();
            if(node.index > 0 || node == root) {
                if(node != root) {
                    String word = words[node.index - 1];
                    if((word.length() > ans.length()) || (word.length() == ans.length() && word.compareTo(ans) < 0)){
                        ans = word;
                    }
                }
                for(Node children : node.map.values()){
                    stack.push(children);
                }
            }
        }
        return ans;
    }
}
