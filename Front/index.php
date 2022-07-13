<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File upload</title>
</head>

<body>
    <form action="http://127.0.0.1:5000/upload" method="post" enctype="multipart/form-data">
        Username: <input type='text' name='username' /><BR>
        Choose csv file: <input type="file" name="file1" accept='.csv' /><BR>
        Choose excel file: <input type="file" name="file2" accept='.xls, .xlsx' /><BR>
        <input type="submit" value="Upload" />
</body>

</html>