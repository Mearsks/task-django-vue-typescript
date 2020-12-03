<template>
    <v-container>
        <v-layout row wrap align-center justify-center fill-height>
            <v-flex xs12 sm8 lg4 md5>
                <v-card class="login-card">
                    <v-card-title>
                        <span class="headline">Login </span>
                    </v-card-title>
                    <v-spacer />
                    <v-card-text>
                        <v-layout
                            row
                            fill-height
                            justify-center
                            align-center
                            v-if="loading"
                        >
                            <v-progress-circular
                                :size="50"
                                color="primary"
                                indeterminate
                            />
                        </v-layout>


                        <v-form v-else ref="form" v-model="valid" lazy-validation>
                            <v-container>

                                <v-text-field
                                    v-model="credentials.username"
                                    :counter="70"
                                    label="ユーザー名"
                                    maxlength="70"
                                    :rules="rules.username"
                                    required
                                    prepend-icon="mdi-account-circle"
                                />

                                <v-text-field
                                    :type="showPassword ? 'text' : 'password'"
                                    v-model="credentials.password"
                                    :counter="20"
                                    label="パスワード"
                                    maxlength="20"
                                    required
                                    :rules="rules.password"
                                    prepend-icon="mdi-lock"
                                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                                    @click:append="showPassword = !showPassword"
                                />
                            </v-container>
                            <v-btn class="primary white--text" :disabled="!valid" @click="login">Login</v-btn>
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>


</template>

<script lang="ts">
import { defineComponent, reactive, ref, toRefs } from '@vue/composition-api';
import Swal from 'sweetalert2';
import { authStore } from "@/store/auth/auth";
import { Credentials } from "@/types";


export default defineComponent({
    name: 'Auth',
    setup() {
        const state = reactive({
            form: ref<any>(null),
            credentials: {} as Credentials | null,
            valid: true,
            loading: false,
            showPassword: false,
            rules: {
                username: [
                    (v: never) => !!v || "ユーザー名は必須です",
                    (v: string[]) => (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません",
                    (v: string) => /^[a-z0-9_]+$/.test(v) || "許可されていない文字が入力されています"
                ],
                password: [
                    (v: never) => !!v || "パスワードは必須です",
                    (v: string[]) => (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません"
                ]
            },
            computed: () => {
                if (authStore.getIsLoginError!.length > 0) {
                    Swal.fire({
                        title: 'Error',
                        text: '入力が間違っています',
                        showConfirmButton: false,
                        showCloseButton: false,
                        timer: 3000
                    });
                }
            }
        });
        const login = () => {
            if (state.form.validate() && state.credentials) {
                state.loading = true;
                authStore.loginUser({username: state.credentials.username, password: state.credentials.password});
            }
        };
        return {
            ...toRefs(state), login
        };
    }
})
;
</script>

