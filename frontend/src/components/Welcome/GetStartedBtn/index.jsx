import { Button} from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    button : {
        backgroundColor: '#0B5688',
        color: 'white',
        fontFamily: 'Viga',
        fontSize: '15px',
        margin: '15px 0',
        padding: '15px 20px',
        borderRadius: '30px',
        "&:hover": {
            transform: 'scale(1.2)',
            backgroundColor: '#0B5688',
            cursor: 'pointer',
        },
    }
}))

const GetStartedBtn = () => {
    const classes = useStyles();

    return (
        <Button href="/register" className={classes.button}>Get Started</Button>
    )
}


export default GetStartedBtn;