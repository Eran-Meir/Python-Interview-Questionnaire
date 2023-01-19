#############################
#    Name:     Eran Meir    #
#    Question:     2        #
#############################

SELECT DEPARTMENT.NAME, COUNT(EMPLOYEE.ID) AS EMPLOYEE_COUNT
    FROM DEPARTMENT
    LEFT JOIN EMPLOYEE ON DEPARTMENT.ID = EMPLOYEE.DEPT_ID
    GROUP BY DEPARTMENT.NAME
    ORDER BY EMPLOYEE_COUNT DESC, DEPARTMENT.NAME ASC