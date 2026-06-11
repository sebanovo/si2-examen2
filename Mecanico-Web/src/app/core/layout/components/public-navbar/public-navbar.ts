import { CommonModule } from "@angular/common";
import {
	Component,
	DOCUMENT,
	HostListener,
	inject,
	signal,
} from "@angular/core";
import { Router, RouterLink, RouterLinkActive } from "@angular/router";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideArrowRight,
	lucideLogIn,
	lucideMenu,
	lucideUserPlus,
	lucideX,
} from "@ng-icons/lucide";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmIconImports } from "@shared/ui/icon";
import {
	PUBLIC_NAVIGATION,
	PublicNavigationItem,
} from "../../constants/public-navigation.constants";

@Component({
	selector: "app-public-navbar",
	imports: [
		CommonModule,
		RouterLink,
		RouterLinkActive,
		NgIcon,
		HlmButtonImports,
		HlmIconImports,
	],
	providers: [
		provideIcons({
			lucideMenu,
			lucideX,
			lucideLogIn,
			lucideUserPlus,
			lucideArrowRight,
		}),
	],
	templateUrl: "./public-navbar.html",
	styleUrl: "./public-navbar.css",
})
export class PublicNavbar {
	private readonly router = inject(Router);
	private readonly document = inject(DOCUMENT);

	readonly navigationItems = PUBLIC_NAVIGATION;

	readonly mobileMenuOpen = signal(false);
	readonly isScrolled = signal(false);

	@HostListener("window:scroll")
	onWindowScroll(): void {
		this.isScrolled.set(window.scrollY > 8);
	}

	toggleMobileMenu(): void {
		this.mobileMenuOpen.update(value => !value);
	}

	closeMobileMenu(): void {
		this.mobileMenuOpen.set(false);
	}

	async onLogoClick(): Promise<void> {
		this.closeMobileMenu();
		await this.navigateToSection("hero");
	}

	async onNavigationItemClick(item: PublicNavigationItem): Promise<void> {
		this.closeMobileMenu();

		if (item.type === "page" && item.route) {
			await this.router.navigateByUrl(item.route);
			return;
		}

		if (item.type === "section" && item.fragment) {
			await this.navigateToSection(item.fragment);
		}
	}

	async onLoginClick(): Promise<void> {
		this.closeMobileMenu();
		await this.router.navigateByUrl("/auth/login");
	}

	async onSignupClick(): Promise<void> {
		this.closeMobileMenu();
		await this.router.navigateByUrl("/auth/signup");
	}

	async onGetStartedClick(): Promise<void> {
		this.closeMobileMenu();
		await this.router.navigateByUrl("/pricing");
	}

	trackByNavigationLabel(_: number, item: PublicNavigationItem): string {
		return item.label;
	}

	private async navigateToSection(sectionId: string): Promise<void> {
		const currentPath = this.router.url.split("#")[0];
		const isHomePage = currentPath === "/";

		if (!isHomePage) {
			await this.router.navigateByUrl("/");
			setTimeout(() => {
				this.scrollToSection(sectionId);
			}, 0);
			return;
		}

		this.scrollToSection(sectionId);
	}

	private scrollToSection(sectionId: string): void {
		requestAnimationFrame(() => {
			const element = this.document.getElementById(sectionId);

			if (!element) {
				return;
			}

			const headerOffset = 80;
			const elementTop = element.getBoundingClientRect().top + window.scrollY;
			const targetTop = Math.max(elementTop - headerOffset, 0);

			window.scrollTo({
				top: targetTop,
				behavior: "smooth",
			});
		});
	}
}
