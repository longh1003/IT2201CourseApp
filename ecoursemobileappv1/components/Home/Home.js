import { FlatList, View } from "react-native"
import { useEffect, useState } from "react"
import { ActivityIndicator, Chip, List, Searchbar } from "react-native-paper";
import Apis, { endpoints } from "../../Apis";
import MyStyles from "../../styles/MyStyles";

const Home = () => {\
    const [categories, setCategories] = useState([]);
    const [courses, setCourses] = useState([]);
    const [loading, setLoading] = useState(false);
    const [page, setPage] = useState(1)

    const [kw, setKw] = useState();

    const loadCates = async () => {
        let res = await Apis.get(endpoints['categories']);
        setCategories(res.data);
    }

    const loadCourses = async () => {
        try {
            setLoading(true);

            let url = `${endpoints['courses']}?page=${}`;
            let res = await Apis.get(url);
            setCourses(res.data.results);
        } catch {

        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        loadCates();
    }, []);

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.subject}>E-COURSE APP ONLINE</Text>
            <View style={MyStyles.row, MyStyles.wrap}>
            {categories.map(c => <Chip key={c.id} style={MyStyles.m}>{c.name}</Chip>)}
            </View>

            <Searchbar placeholder="Tìm kiếm khóa học..." onChangeText={setKw} value={kw}></Searchbar>

            {loading && <ActivityIndicator/>}
            <FlatList data={courses} renderItem={({item}) => <List.Item title={item.subject} description={item.created_date} left={() =>}></List.Item>}></FlatList>
        </View>
        );
}

export default Home;