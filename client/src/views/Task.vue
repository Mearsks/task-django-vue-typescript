<template>
    <div>
        Task Page
    </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from '@vue/composition-api';
import router from "@/router";
import { authStore } from "@/store/auth/auth";


export default defineComponent({
    name: 'Task',
    setup() {
        const checkLoggedIn = () => {
            if (authStore.getIsUserLoggedIn) {
                router.push({name: 'Auth'});
            }
        };
        onMounted(() => {
            checkLoggedIn()
        });
    }
})
</script>

