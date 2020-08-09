import React from "react";
import { View, Text } from "react-native";

import PageHeader from "../../components/PageHeader";
import TeacherItem from "../../components/TeacherItem";

import styles from "./styles";

const TeacherList = () => {
  return (
    <View style={styles.container}>
      <PageHeader title="Proffys disponíveis" />
      <TeacherItem />
      <TeacherItem />
      <TeacherItem />
      <TeacherItem />
    </View>
  );
};

export default TeacherList;
