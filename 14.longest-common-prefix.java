import java.util.HashMap;

/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (33.19%)
 * Total Accepted:    435.4K
 * Total Submissions: 1.3M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 * 
 * If there is no common prefix, return an empty string "".
 * 
 * Example 1:
 * 
 * 
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 * 
 * 
 * Note:
 * 
 * All given inputs are in lowercase letters a-z.
 * 
 */
class Solution {
    public String longestCommonPrefix(String[] strs) {
        Trie trie = new Trie();
        int index = 0;
        for(int i = 0; i < strs.length; i++) {
            trie.insertWord(strs[i], ++index);
        }
        return trie.findPrefix();
    }
   
}
class Trie {
    Node node;
    Trie(){
        node = new Node('0');
    }
    void insertWord(String word, int index) {
        Node curr = node;
        for(char c : word.toCharArray()){  
            curr.map.putIfAbsent(c, new Node(c));
            curr = curr.map.get(c);
            System.out.println("char:" + c);
        }
    }

    String findPrefix(){
        String prefix = "";
        Node cur = node;
        while(cur.map.values().size() == 1) {
            prefix += cur.c;
            cur = cur.map.values().toArray()[0];
        }
        return prefix.substring(1);
    }
} 

class Node {
    HashMap<Character, Node> map = new HashMap<Character, Node>();
    char c;
    Node(char c){
        this.c = c;
    }
}