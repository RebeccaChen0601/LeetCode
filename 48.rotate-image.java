/*
 * @lc app=leetcode id=48 lang=java
 *
 * [48] Rotate Image
 */
public class Solution {
    public void rotate(int[][] matrix) {
        for(int i = 0; i < matrix.length; i++){
            for(int j = i; j < matrix[0].length; j++){
                swap(matrix, i, j, j, i);
            }
        }
        for(int i =0 ; i<matrix.length; i++){
            for(int j = 0; j<matrix.length/2; j++){
               swap(matrix, i, j, i, matrix.length - j - 1);
            }
        }
    }
    void swap(int[][] matrix, int i, int j, int a, int b){
        int temp = matrix[i][j]; 
        matrix[i][j] = matrix[a][b];
        matrix[a][b] = temp;
    }
}

