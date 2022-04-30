import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { InputLabel, Select, Button, Box, Typography, TextField, Link, CssBaseline, DialogTitle } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import * as userService from '../../api/user.service';

const useStyles = makeStyles((theme) => ({
    button: {
        margin: '20px auto',
        backgroundColor: '#0B568899',
        borderRadius: '10px',
        fontFamily: 'Viga',
        width: '100px'
    },
    form: {
        width: '80%',
        margin: '5px 10px',
    },
    box: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center'
    }
}))


const StudentEditForm = (props) => {

    const classes = useStyles();
    const [name, setName] = useState('')
    const [grade, setGrade] = useState('')
    const [avatar, setAvatar] = useState('')
    const navigate = useNavigate()

    const handleSubmit = async () => {
        let UpdateStudent = {name, grade, avatar, instuctor : localStorage.getItem('user')}
        console.log(UpdateStudent)
        await userService.editStudent(props.editStudentData.id, UpdateStudent).then((res) => {
            // console.log(res)
            navigate(0)
        })
        .catch(err => console.log(err))
    }

    return (
    <>
        <DialogTitle align="center">
            <Typography variant='h5'>Edit Student</Typography>
        </DialogTitle>
        <Box className={classes.box} component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <InputLabel className={classes.form}>Name</InputLabel>
            <TextField
                className={classes.form}
                required
                name="name"
                autoFocus
                variant='filled'
                margin="normal"
                value = {name}
                placeholder = {props.editStudentData.name}
                onChange={(e)=> setName(e.target.value)}/>
            <InputLabel className={classes.form}>Grade</InputLabel>
            <Select 
                className={classes.form}
                native value={grade}
                variant='filled'
                required
                onChange={(e)=> setGrade(e.target.value)}>
                <option>---</option>
                <option value="Pre-K">Pre-K</option>
                <option value="Kindergarten">Kindergarten</option>
                <option value="1st Grade">1st Grade</option>
                <option value="2nd Grade">2nd Grade</option>
                <option value="3rd Grade">3rd Grade</option>
            </Select>
            <InputLabel className={classes.form} >Avatar</InputLabel>
            <Select 
                className={classes.form}
                native value={avatar}
                variant='filled'
                required
                onChange={(e)=> setAvatar(e.target.value)}>
                <option>---</option>
                <option value="1">avatar1</option>
            </Select>
            <div>
                <Button className={classes.button} type="submit">Add</Button>
            </div>
            <Link onClick={props.handleClose}>Cancel</Link>
        </Box>
    </>
    
    )
}

export default StudentEditForm;