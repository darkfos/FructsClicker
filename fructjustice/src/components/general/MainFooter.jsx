import "./MainFooter.css";

//Images
import banana from "../../static/img/banana.png";
import tangerine from "../../static/img/tangerine.png";
import kiwi from "../../static/img/kiwi.png";
import { Link } from "react-router-dom";

export default function GeneralFooter() {
    return (
        <footer className="footer_main">
            <ul>
                <li>
                    <div className="attrmenu">
                        <img src={banana} alt="Бананчик"/>
                        <Link to="/">Игра</Link>
                    </div>
                </li>
                <li>
                    <div className="attrmenu">
                        <img src={tangerine} alt="Мандарин" />
                        <Link to="/fruct-shop">Магазин</Link>
                    </div>
                </li>
                <li>
                    <div className="attrmenu">
                        <img src={kiwi} alt="Киви" />
                        <Link to="/profile">Профиль</Link>
                    </div>
                </li>
            </ul>
        </footer>
    )
}