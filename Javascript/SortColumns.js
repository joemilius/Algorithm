function sortColumns(){
    
}

/*
Write a function sortColumns() that accepts one argument, a string representation of a data table, 
and returns the data sorted by the column headers (the values in the first row).  
 
The sorting should be case-insensitive alphabetical (A-Z). The format of the data tables is as follows: 
 
"steve,Andrew,michael,Yamuna,Harrison,Leslie\n3112,21352,123412,14134,1235,51
325\n2,6,3,4,1,5" 
 
Rows are separated by the newline character “\n”, so the above represents the following table: 
 
| steve | Andrew | michael | Yamuna | Harrison | Leslie | 
| 3112  | 21352  | 123412  | 14134  | 1235     | 51325  | 
| 2     | 6      | 3       | 4      | 1        | 5      | 
 
If sorting the table by the column headers, the table would look like this: 
 
| Andrew | Harrison | Leslie | michael | steve | Yamuna | 
| 21352  | 1235     | 51325  | 123412  | 3112  | 14134  | 
| 6      | 1        | 5      | 3       | 2     | 4      | 
 
The string representation of the above table would be: 
 
"Andrew,Harrison,Leslie,michael,steve,Yamuna\n21352,1235,51325,123412,3112,14
134\n6,1,5,3,2,4"
*/