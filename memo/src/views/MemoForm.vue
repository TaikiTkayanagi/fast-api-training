<script setup lang="ts">
import { useMemoForm } from '@/stores/memoForm';
import { useRouter } from 'vue-router';

const memoFormStore = useMemoForm();
const router = useRouter();

const click = async (e: Event) => {
    e.preventDefault();
    await memoFormStore.post();
    memoFormStore.title
    router.push('/');
}
</script>

<template>
    <div>
        <h1>Memo Form</h1>
        <form>
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" v-model="memoFormStore.title" />

            <label for="content">Content:</label>
            <textarea id="content" name="content" v-model="memoFormStore.content"></textarea>

            <button type="submit" v-on:click="click">Submit</button>
        </form>
    </div>
</template>