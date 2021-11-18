function sortColumns(str){
let newArr = []
let result = []
let table = str.split('\n').map(word => word.split(','))

    for(let i = 0; i < table[0].length; i++){
        let object = new Object
        object.name = table[0][i]
        object.large = table[1][i]
        object.small = table[2][i]
        newArr.push(object)
    }

    newArr.sort(
        function(a, b) {
            if(a.name.toLowerCase() < b.name.toLowerCase()) return -1;
            if(a.name.toLowerCase() > b.name.toLowerCase()) return 1;
        }
    )
    result.push[newArr.map(item => item.name) + '\\n']
    result.push[newArr.map(item => item.large) + '\\n']
    result.push[newArr.map(item => item.small)]

    return result.join()

}

sortColumns("steve,Andrew,michael,Yamuna,Harrison,Leslie\n3112,21352,123412,14134,1235,51325\n2,6,3,4,1,5")

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