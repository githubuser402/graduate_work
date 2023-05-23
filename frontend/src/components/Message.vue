<template>
    <div :style="['--text-color: ${color}',]" v-bind:class="[(this.show ? 'show-message' : 'hide-message'), 'message-box']" on-click="">
        <p>{{ message }}</p>
        {{ this.elementStyling }}
    </div>
</template>

<script>
export default {
    name: 'Message',
    props: {
        message: {
            type: String,
            required: true,
        },
        color: {
            type: String,
            default: 'yellow',
        },
        show: {
            type: Boolean,
            required: true,
        },
    },
    data() {
        return {
        }
    },
    computed: {
    },
};
</script>

<style scoped>
.message-box {
    border: 1px solid black;
    color: var(--text-color);
    border-radius: 0px;
    margin: 0 auto;
    width: 50%;
    padding: 5px;
    text-align: center;
}

.show-message {
    display: block;
}

.hide-message {
    display: none;
}

h1 {
    color: red;
}
</style>