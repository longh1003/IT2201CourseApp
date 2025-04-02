import { View } from "react-native"
import { useEffect, useState } from "react"
import { Chip } from "react-native-paper";
import Apis, { endpoints } from "../../Apis";
import MyStyles from "../../styles/MyStyles";

const Home = () => {\
    const [categories, setCategories] = useState([]);

    const loadCates = async () => {
        let res = await Apis.get(endpoints['categories']);
        setCategories(res.data);
    }

    useEffect(() => {
        loadCates();
    }, []);

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.subject}>E-COURSE APP ONLINE</Text>
            <View style={MyStyles.rows}></View>
            {categories.map(c => <Chip key={c.id} style={MyStyles.m}>{c.name}</Chip>)}
        </View>
        );
}

export default Home;