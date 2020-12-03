import store from '@/store';
import { Module, VuexModule, getModule, Action, Mutation } from "vuex-module-decorators";
import axios from "axios";
import router from "@/router";
import { Credentials } from "@/types";


@Module({ dynamic: true, store, name: 'auth', namespaced: true })
class AuthModule extends VuexModule {

    private userToken: string[] | null = [];
    private isLoginError: string[] | null = []

    @Mutation
    updateUser(user: string[]) {
        this.userToken = user
        console.log(this.userToken);
    }

    @Action
    async loginUser({username, password}: {username: string; password: string}) {
        try {
            const res  = await axios.post('http://localhost:8000/auth/', {username, password});
            await router.push({name: 'Task'})
            console.log(res.data);
        } catch (error) {
            const { status, statusText } = error.response;
            console.log(status, statusText);
            console.log(error);
        }
    }


    get getIsUserLoggedIn() {
        return this.userToken;
    }

    get getIsLoginError() {
        return this.isLoginError
    }
}


export const authStore = getModule(AuthModule);
