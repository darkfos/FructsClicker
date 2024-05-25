import {Fragment} from "react";
import GeneralFooter from "../components/general/MainFooter";
import { Outlet } from "react-router-dom";


export default function Profile() {
    return (
        <div className="df">
            <body>
                <h2>Ваш профиль</h2>
                <p>Profile</p>
            </body>
            <GeneralFooter />
        </div>
    )
}